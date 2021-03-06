%global packname  SPOT
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1550
Release:          1%{?dist}
Summary:          Sequential Parameter Optimization

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-graphics R-fields R-rpart R-maptree R-colorspace R-gtools R-car 

BuildRequires:    R-devel tex(latex) R-lattice R-graphics R-fields R-rpart R-maptree R-colorspace R-gtools R-car 

%description
R-Package for Sequential Parameter Optimization Toolbox

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1550-1
- initial package for Fedora