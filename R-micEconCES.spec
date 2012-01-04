%global packname  micEconCES
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.4
Release:          1%{?dist}
Summary:          Analysis with the Constant Elasticity of Scale (CES) function

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-systemfit R-miscTools R-micEcon R-minpack.lm R-DEoptim 

BuildRequires:    R-devel tex(latex) R-systemfit R-miscTools R-micEcon R-minpack.lm R-DEoptim 

%description
Tools for economic analysis and economic modelling with a Constant
Elasticity of Scale (CES) function

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.4-1
- initial package for Fedora