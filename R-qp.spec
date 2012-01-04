%global packname  qp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          q-order partial correlation graph search algorithm

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package is deprecated and it is now only a stub for the newer version
called qpgraph available through the Bioconductor project. The q-order
partial correlation graph search algorithm, q-partial, or qp, algorithm
for short, is a robust procedure for structure learning of undirected
Gaussian graphical Markov models from "small n, large p" data, that is,
multivariate normal data coming from a number of random variables p larger
than the number of multidimensional data points n as in the case of, e.g.,
microarray data.

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
%doc %{rlibdir}/qp/DESCRIPTION
%doc %{rlibdir}/qp/html
%{rlibdir}/qp/INDEX
%{rlibdir}/qp/data
%{rlibdir}/qp/help
%{rlibdir}/qp/Meta
%{rlibdir}/qp/R
%{rlibdir}/qp/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora