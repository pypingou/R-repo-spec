%global packname  review
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.4.1
Release:          1%{?dist}
Summary:          Manage Review Logs

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-XML R-Hmisc 

BuildRequires:    R-devel tex(latex) R-XML R-Hmisc 

%description
Functions for managing logs of reviews of subversioned files.

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
%doc %{rlibdir}/review/DESCRIPTION
%doc %{rlibdir}/review/html
%{rlibdir}/review/R
%{rlibdir}/review/review.R
%{rlibdir}/review/Meta
%{rlibdir}/review/help
%{rlibdir}/review/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.1-1
- initial package for Fedora