%global packname  eco
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.1.5
Release:          1%{?dist}
Summary:          R Package for Ecological Inference in 2x2 Tables

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
eco is a publicly available R package that implements the Bayesian and
likelihood methods proposed in Imai, Lu, and Strauss (2008) for ecological
inference in $2 \times 2$ tables as well as the method of bounds
introduced by Duncan and Davis (1953). The package fits both parametric
and nonparametric models using either the Expectation-Maximization
algorithms (for likelihood models) or the Markov chain Monte Carlo
algorithms (for Bayesian models).  For all models, the individual-level
data can be directly incorporated into the estimation whenever such data
are available. Along with in-sample and out-of-sample predictions, the
package also provides a functionality which allows one to quantify the
effect of data aggregation on parameter estimation and hypothesis testing
under the parametric likelihood models.

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
%doc %{rlibdir}/eco/html
%doc %{rlibdir}/eco/CITATION
%doc %{rlibdir}/eco/DESCRIPTION
%{rlibdir}/eco/NAMESPACE
%{rlibdir}/eco/R
%{rlibdir}/eco/help
%{rlibdir}/eco/data
%{rlibdir}/eco/INDEX
%{rlibdir}/eco/libs
%{rlibdir}/eco/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.1.5-1
- initial package for Fedora