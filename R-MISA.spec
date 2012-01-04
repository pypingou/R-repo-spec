%global packname  MISA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.11.1.1.0.1
Release:          1%{?dist}
Summary:          Bayesian Model Search and Multilevel Inference for SNP Association Studies

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.11.1-1.0.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-coda 

BuildRequires:    R-devel tex(latex) R-coda 

%description
The functions in this package focus on intermediate throughput
case-control association studies, where the outcome of interest is often a
binary disease state and where the genetic markers have been chosen to
capture variation in a set of related genes, such as those involved in a
specific biochemical pathway. Given this data, we are interested in
addressing two questions: "To what extent does the data support an overall
association between the pathway and outcome of interest?" and "Which
markers or genes are most likely to be driving this association?" To
address both of these questions,this package performs a Bayesian model
search technique that utilizes Evolutionary Monte Carlo and searches over
models including main effects of all genetic markers and marker-specific
genetic effects in a computationally efficient manner.  The package
incorporates functions that perform a marginal screen on the genetic
markers, summarize the output of the model search algorithm, including
image plots of the models with the highest posterior probability, marginal
summaries of SNP and gene inclusion probabilities and Bayes Factors, and
global summaries of the posterior probability and Bayes Factor giving
evidence of an association in the set of SNPs of interest.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.11.1.1.0.1-1
- initial package for Fedora