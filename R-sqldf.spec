%global packname  sqldf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.5
Release:          1%{?dist}
Summary:          Perform SQL Selects on R Data Frames

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-DBI R-RSQLite R-RSQLite.extfuns R-gsubfn R-proto R-chron 


BuildRequires:    R-devel tex(latex) R-DBI R-RSQLite R-RSQLite.extfuns R-gsubfn R-proto R-chron



%description
Description: Manipulate R data frames using SQL.

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
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.5-1
- initial package for Fedora