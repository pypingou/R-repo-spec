%global packname  topicmodels
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Topic models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lasso2 R-stats4 R-methods R-modeltools R-slam R-tm 


BuildRequires:    R-devel tex(latex) R-lasso2 R-stats4 R-methods R-modeltools R-slam R-tm



%description
Provides an interface to the C code for Latent Dirichlet Allocation (LDA)
models and Correlated Topics Models (CTM) by David M. Blei and co-authors
and the C++ code for fitting LDA models using Gibbs sampling by Xuan-Hieu
Phan and co-authors.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora