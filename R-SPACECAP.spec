%global packname  SPACECAP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          A Program to Estimate Animal Abundance and Density using Spatially-Explicit Capture-Recapture

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-TeachingDemos 

BuildRequires:    R-devel tex(latex) R-tcltk R-TeachingDemos 

%description
SPACECAP is a user-friendly software package for estimating animal
densities using closed model capture-recapture sampling based on
photographic captures using Bayesian spatially-explicit capture-recapture
models. This approach offers advantage such as: substantially dealing with
problems posed by individual heterogeneity in capture probabilities in
conventional capture-recapture analyses. It also offers non-asymptotic
inferences which are more appropriate for small samples of capture data
typical of photo-capture studies.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4-1
- initial package for Fedora