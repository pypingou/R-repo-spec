%global packname  rv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Simulation-based random variable object class in R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-utils R-grDevices R-graphics 

BuildRequires:    R-devel tex(latex) R-stats R-utils R-grDevices R-graphics 

%description
Simulation-based random variable object class

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
%doc %{rlibdir}/rv/doc
%doc %{rlibdir}/rv/DESCRIPTION
%doc %{rlibdir}/rv/CITATION
%doc %{rlibdir}/rv/html
%{rlibdir}/rv/Meta
%{rlibdir}/rv/INDEX
%{rlibdir}/rv/NAMESPACE
%{rlibdir}/rv/R
%{rlibdir}/rv/help
%{rlibdir}/rv/demo
%{rlibdir}/rv/ChangeLog

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora