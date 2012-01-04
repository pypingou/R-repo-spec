%global packname  NetworkAnalysis
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Statistical inference on populations of weighted or unweighted networks.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rcpp R-nlme R-lme4 R-igraph R-inline 


BuildRequires:    R-devel tex(latex) R-Rcpp R-nlme R-lme4 R-igraph R-inline



%description
Network analysis refers to the utilization of graph theory for the
analysis of a range of different types of connectivity data. The set of
objects contained in this package will be particularly useful for the
analysis of groups of networks in neuroimaging, where several populations
of subject-specific networks are available. Future versions will include
the derivation of SPNs (statistical parametric networks). This revised
version of the package now includes C++ codes, which permit to speed up
the computational cost of the main cost-integration routines.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora