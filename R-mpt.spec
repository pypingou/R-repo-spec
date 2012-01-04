%global packname  mpt
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Multinomial Processing Tree (MPT) Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Fitting and testing multinomial processing tree models, a class of
statistical models for categorical data with latent parameters.  These
parameters are the link probabilities of a tree-like graph and represent
the cognitive processing steps executed to arrive at observable response
categories (Batchelder & Riefer, 1999; Erdfelder et al., 2009; Riefer &
Batchelder, 1988).

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
%doc %{rlibdir}/mpt/DESCRIPTION
%doc %{rlibdir}/mpt/html
%{rlibdir}/mpt/data
%{rlibdir}/mpt/Meta
%{rlibdir}/mpt/NAMESPACE
%{rlibdir}/mpt/INDEX
%{rlibdir}/mpt/R
%{rlibdir}/mpt/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.0-1
- initial package for Fedora