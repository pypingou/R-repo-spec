%global packname  MasterBayes
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.47
Release:          1%{?dist}
Summary:          ML and MCMC Methods for Pedigree Reconstruction and Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-coda R-genetics R-gtools R-kinship 


BuildRequires:    R-devel tex(latex) R-coda R-genetics R-gtools R-kinship



%description
The primary aim of MasterBayes is to use MCMC techniques to integrate over
uncertainty in pedigree configurations estimated from molecular markers
and phenotypic data.  Emphasis is put on the marginal distribution of
parameters that relate the phenotypic data to the pedigree. All simulation
is done in compiled C++ for efficency.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.47-1
- initial package for Fedora