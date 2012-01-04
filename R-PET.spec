%global packname  PET
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.9
Release:          1%{?dist}
Summary:          Simulation and Reconstruction of PET Images

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-adimpro 

BuildRequires:    R-devel tex(latex) R-adimpro 

%description
This package implements different analytic/direct and iterative
reconstruction methods of Peter Toft. It also offer the possibility to
simulate PET data.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.9-1
- initial package for Fedora