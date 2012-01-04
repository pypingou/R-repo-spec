%global packname  SGP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.1.0
Release:          1%{?dist}
Summary:          An R Package for the Calculation and Visualization of Student Growth Percentiles & Percentile Growth Trajectories.

Group:            Applications/Engineering 
License:          CC BY-SA 3.0 US | CC BY-NC-SA 3.0 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-1.0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot R-colorspace R-data.table R-foreach R-grid R-gridBase R-methods R-plyr R-randomNames R-quantreg R-splines 


BuildRequires:    R-devel tex(latex) R-boot R-colorspace R-data.table R-foreach R-grid R-gridBase R-methods R-plyr R-randomNames R-quantreg R-splines



%description
Functions to calculate student growth percentiles and percentile growth
projections/trajectories for students using large scale, longitudinal
assessment data.  Functions use quantile regression to estimate the
conditional density associated with each student's achievement history. 
Percentile growth projections/trajectories are calculated using the
coefficient matrices derived from the quantile regression analyses and
specify what percentile growth is required for students to reach future
achievement targets.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.1.0-1
- initial package for Fedora