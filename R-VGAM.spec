%global packname  VGAM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.4
Release:          1%{?dist}
Summary:          Vector Generalized Linear and Additive Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-splines R-methods R-stats R-stats4 

BuildRequires:    R-devel tex(latex) R-splines R-methods R-stats R-stats4 

%description
Vector generalized linear and additive models, and associated models
(Reduced-Rank VGLMs, Quadratic RR-VGLMs, Reduced-Rank VGAMs). This package
fits many models and distribution by maximum likelihood estimation (MLE)
or penalized MLE. Also fits constrained ordination models in ecology.

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
%doc %{rlibdir}/VGAM/NEWS
%doc %{rlibdir}/VGAM/html
%doc %{rlibdir}/VGAM/CITATION
%doc %{rlibdir}/VGAM/doc
%doc %{rlibdir}/VGAM/DESCRIPTION
%{rlibdir}/VGAM/INDEX
%{rlibdir}/VGAM/Meta
%{rlibdir}/VGAM/NAMESPACE
%{rlibdir}/VGAM/libs
%{rlibdir}/VGAM/R
%{rlibdir}/VGAM/data
%{rlibdir}/VGAM/demo
RPM build errors:
%{rlibdir}/VGAM/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.4-1
- initial package for Fedora