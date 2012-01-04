%global packname  TIMP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.1
Release:          1%{?dist}
Summary:          a problem solving environment for fitting separable nonlinear models in physics and chemistry applications

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-tcltk R-vcd R-fields R-gplots R-splines R-gclus R-nnls R-odesolve R-minpack.lm 


BuildRequires:    R-devel tex(latex) R-methods R-tcltk R-vcd R-fields R-gplots R-splines R-gclus R-nnls R-odesolve R-minpack.lm



%description
TIMP is a problem solving environment for fitting separable nonlinear
models to measurements arising in physics and chemistry experiments, and
has been extensively applied to time-resolved spectroscopy and FLIM-FRET

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.1-1
- initial package for Fedora