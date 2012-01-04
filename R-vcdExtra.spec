%global packname  vcdExtra
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          vcd additions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-vcd R-gnm 


BuildRequires:    R-devel tex(latex) R-vcd R-gnm



%description
Provides additional data sets, methods and documentation to complement the
vcd package for Visualizing Categorical Data and the gnm package for
Generalized Nonlinear Models. In particular, vcdExtra extends mosaic,
assoc and sieve plots from vcd to handle glm() and gnm() models and adds a
3D version in mosaic3d.

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
%doc %{rlibdir}/vcdExtra/NEWS
%doc %{rlibdir}/vcdExtra/html
%doc %{rlibdir}/vcdExtra/doc
%doc %{rlibdir}/vcdExtra/DESCRIPTION
%{rlibdir}/vcdExtra/INDEX
%{rlibdir}/vcdExtra/Meta
%{rlibdir}/vcdExtra/data
%{rlibdir}/vcdExtra/help
%{rlibdir}/vcdExtra/R
%{rlibdir}/vcdExtra/NAMESPACE
%{rlibdir}/vcdExtra/demo

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.2-1
- initial package for Fedora