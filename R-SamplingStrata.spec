%global packname  SamplingStrata
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Optimal stratification of sampling frames for multipurpose sampling surveys

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
In the field of sampling design (in particular for stratified sampling),
this package offers an approach for the determination of the best
stratification of a sampling frame, the one that ensures the minimum
sample size under the condition to satisfy precision constraints in a
multivariate and multidomain case. This approach is based on the use of
the genetic algorithm: each solution (i.e. a particular partition in
strata of the sampling frame) is considered as an individual in a
population; the fitness of all individuals is evaluated by calculating
(using the Bethel-Chromy algorithm) the sampling size satisfying accuracy
constraints on the target estimates. Functions in the package allows to:
(a) analyse the obtained results of the optimisation step; (b) assign the
new strata labels to the sampling frame; (c) select a sample from the new
frame accordingly to the best allocation. There is also a function that
allows to build the most important input to the optimisation step, i.e.
the "strata" dataframe, containing information (means and standard errors)
regarding the distributions of the target variables in the different
strata, using the sampling frame or using data from previous rounds of the
same survey.

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
%doc %{rlibdir}/SamplingStrata/doc
%doc %{rlibdir}/SamplingStrata/DESCRIPTION
%doc %{rlibdir}/SamplingStrata/html
%{rlibdir}/SamplingStrata/R
%{rlibdir}/SamplingStrata/INDEX
%{rlibdir}/SamplingStrata/data
%{rlibdir}/SamplingStrata/Meta
%{rlibdir}/SamplingStrata/help
%{rlibdir}/SamplingStrata/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.1-1
- initial package for Fedora