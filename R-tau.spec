%global packname  tau
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.12
Release:          1%{?dist}
Summary:          Text Analysis Utilities

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Utilities for text analysis

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
%doc %{rlibdir}/tau/DESCRIPTION
%doc %{rlibdir}/tau/html
%{rlibdir}/tau/help
%{rlibdir}/tau/INDEX
%{rlibdir}/tau/Meta
%{rlibdir}/tau/libs
RPM build errors:
%{rlibdir}/tau/R
%{rlibdir}/tau/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.12-1
- initial package for Fedora