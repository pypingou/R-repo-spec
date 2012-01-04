%global packname  ICE
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.61
Release:          1%{?dist}
Summary:          Iterated Conditional Expectation

Group:            Applications/Engineering 
License:          GNU Public License
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-KernSmooth 

BuildRequires:    R-devel tex(latex) R-KernSmooth 

%description
Kernel Estimators for Interval-Censored Data

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
%doc %{rlibdir}/ICE/DESCRIPTION
%doc %{rlibdir}/ICE/html
%{rlibdir}/ICE/NAMESPACE
%{rlibdir}/ICE/data
%{rlibdir}/ICE/libs
%{rlibdir}/ICE/INDEX
%{rlibdir}/ICE/help
%{rlibdir}/ICE/Meta
%{rlibdir}/ICE/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.61-1
- initial package for Fedora