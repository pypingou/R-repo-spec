%global packname  randomNames
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.3
Release:          1%{?dist}
Summary:          Random name generating function and data set

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-data.table 

BuildRequires:    R-devel tex(latex) R-data.table 

%description
Function to generate random gender and ethnicity correct first and/or last
names. Names are chosen proportionally based upon their probability of
appearing in a large scale data base of real names.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/randomNames/html
%doc %{rlibdir}/randomNames/CITATION
%doc %{rlibdir}/randomNames/NEWS
%doc %{rlibdir}/randomNames/DESCRIPTION
%{rlibdir}/randomNames/help
%{rlibdir}/randomNames/data
%{rlibdir}/randomNames/Meta
%{rlibdir}/randomNames/R
%{rlibdir}/randomNames/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.3-1
- initial package for Fedora