%global packname  bridge
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18.0
Release:          1%{?dist}
Summary:          Bayesian Robust Inference for Differential Gene Expression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rama 

BuildRequires:    R-devel tex(latex) R-rama 

%description
Test for differentially expressed genes with microarray data. This package
can be used with both cDNA microarrays or Affymetrix chip. The packge fits
a robust Bayesian hierarchical model for testing for differential
expression. Outliers are modeled explicitly using a $t$-distribution. The
model includes an exchangeable prior for the variances which allow
different variances for the genes but still shrink extreme empirical
variances. Our model can be used for testing for differentially expressed
genes among multiple samples, and can distinguish between the different
possible patterns of differential expression when there are three or more
samples. Parameter estimation is carried out using a novel version of
Markov Chain Monte Carlo that is appropriate when the model puts mass on
subspaces of the full parameter space.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18.0-1
- initial package for Fedora