%global packname  SixSigma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Six Sigma Tools for Quality and Process Improvement

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-grid R-ggplot2 R-nortest 

BuildRequires:    R-devel tex(latex) R-lattice R-grid R-ggplot2 R-nortest 

%description
This package contains functions and utilities to perform Statistical
Analysis for Six Sigma methodology. Through its outline DMAIC (Define,
Measure, Analyze, Improve, Control), you can manage several Quality
Management studies. The current version includes Capability Analysis, Gage
R&R Study, Confidence Interval, Cause-and-effect diagram and Process Map.
There will be new functions very soon for Capability Analysis, Control
Charts, Reliability, OC Curves, Regression and Design of Experiments. See
?SixSigma for an Introduction.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.0-1
- initial package for Fedora