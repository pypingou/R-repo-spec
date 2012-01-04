%global packname  spatstat
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24.2
Release:          1%{?dist}
Summary:          Spatial Point Pattern analysis, model-fitting, simulation, tests

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.24-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics R-utils R-mgcv R-deldir 

BuildRequires:    R-devel tex(latex) R-stats R-graphics R-utils R-mgcv R-deldir 

%description
A package for analysing spatial data, mainly Spatial Point	Patterns,
including multitype/marked points and spatial covariates, in any
two-dimensional spatial region. Also supports three-dimensional point
patterns, and space-time point patterns in any number of dimensions.
Contains over 1000 functions for plotting spatial data, exploratory data
analysis, model-fitting, simulation, spatial sampling, model diagnostics,
and formal inference. Data types include point patterns, line segment
patterns, spatial windows, pixel images and tessellations. Exploratory
methods include K-functions, nearest neighbour distance and empty space
statistics, Fry plots, pair correlation function, kernel smoothed
intensity, relative risk estimation with cross-validated bandwidth
selection, mark correlation functions, segregation indices, mark
dependence diagnostics etc. Point process models can be fitted to point
pattern data using functions ppm, kppm, slrm similar to glm. Models may
include dependence on covariates, interpoint interaction, cluster
formation and dependence on marks. Fitted models can be simulated
automatically. Also provides facilities for formal inference (such as
chi-squared tests) and model diagnostics (including simulation envelopes,
residuals, residual plots and Q-Q plots).

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
%doc %{rlibdir}/spatstat/CITATION
%doc %{rlibdir}/spatstat/doc
%doc %{rlibdir}/spatstat/NEWS
%doc %{rlibdir}/spatstat/DESCRIPTION
%doc %{rlibdir}/spatstat/html
%{rlibdir}/spatstat/ratfor
%{rlibdir}/spatstat/INDEX
%{rlibdir}/spatstat/R
%{rlibdir}/spatstat/data
%{rlibdir}/spatstat/help
%{rlibdir}/spatstat/demo
%{rlibdir}/spatstat/NAMESPACE
%{rlibdir}/spatstat/libs
%{rlibdir}/spatstat/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24.2-1
- initial package for Fedora