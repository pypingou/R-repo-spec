%global packname  survey
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.26.1
Release:          1%{?dist}
Summary:          analysis of complex survey samples

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.26-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Summary statistics, two-sample tests, generalised linear models,
cumulative link models, Cox models, loglinear models, and general maximum
pseudolikelihood estimation for multistage stratified, cluster-sampled,
unequally weighted survey samples. Variances by Taylor series
linearisation or replicate weights. Post-stratification, calibration, and
raking. Two-phase subsampling designs. Graphics. Predictive margins by
direct standardization. PPS sampling without replacement. Principal
components, factor analysis.

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
%doc %{rlibdir}/survey/DESCRIPTION
%doc %{rlibdir}/survey/NEWS
%doc %{rlibdir}/survey/CITATION
%doc %{rlibdir}/survey/COPYING
%doc %{rlibdir}/survey/html
%doc %{rlibdir}/survey/doc
%{rlibdir}/survey/BUGS
%{rlibdir}/survey/Meta
%{rlibdir}/survey/data
%{rlibdir}/survey/disclaimer
%{rlibdir}/survey/api.db
%{rlibdir}/survey/porting.to.S
RPM build errors:
%{rlibdir}/survey/NAMESPACE
%{rlibdir}/survey/ucla-examples.pdf
%{rlibdir}/survey/INDEX
%{rlibdir}/survey/R
%{rlibdir}/survey/help
%{rlibdir}/survey/twostage.pdf

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.26.1-1
- initial package for Fedora