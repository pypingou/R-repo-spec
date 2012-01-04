%global packname  integrativeME
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          integrative mixture of experts

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mclust R-mixOmics R-randomForest 


BuildRequires:    R-devel tex(latex) R-mclust R-mixOmics R-randomForest



%description
Mixture of experts models (Jacobs et al., 1991) were introduced to account
for nonlinearities and other complexities in the data. It is based on a
divide-and-conquer strategy. Mixture of experts are of interest due to
their wide applicability and the advantages of fast learning via the
expectation-maximization (EM) algorithm. We have extended and implemented
mixture of experts to combine categorical clinical factors and continuous
microarray data in a binary classification framework to analyze cancer
studies. To provide a hybrid signature of clinical factors and gene
markers, we propose to apply different gene selection procedures as a
first step.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora