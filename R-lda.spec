%global packname  lda
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Collapsed Gibbs sampling methods for topic models.

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package implements latent Dirichlet allocation (LDA) and related
models.  This includes (but is not limited to) sLDA, corrLDA, and the
mixed-membership stochastic blockmodel. Inference for all of these models
is implemented via a fast collapsed Gibbs sampler writtten in C.  Utility
functions for reading/writing data typically used in topic models, as well
as tools for examining posterior distributions are also included.

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
%doc %{rlibdir}/lda/DESCRIPTION
%doc %{rlibdir}/lda/html
%{rlibdir}/lda/NAMESPACE
%{rlibdir}/lda/INDEX
%{rlibdir}/lda/R
%{rlibdir}/lda/help
%{rlibdir}/lda/libs
%{rlibdir}/lda/data
%{rlibdir}/lda/Meta
%{rlibdir}/lda/demo

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora