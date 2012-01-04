%global packname  gRapHD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Efficient selection of undirected graphical models for high-dimensional datasets

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-graph 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-graph 


%description
gRapHD is designed for efficient selection of high-dimensional undirected
graphical models. The package provides tools for selecting trees, forests
and decomposable models minimizing information criteria such as AIC or
BIC, and for displaying the independence graphs of the models. It has also
some useful tools for analysing graphical structures. It supports the use
of discrete, continuous, or both types of variables.

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
%doc %{rlibdir}/gRapHD/html
%doc %{rlibdir}/gRapHD/DESCRIPTION
%doc %{rlibdir}/gRapHD/doc
%doc %{rlibdir}/gRapHD/CITATION
%{rlibdir}/gRapHD/NAMESPACE
%{rlibdir}/gRapHD/INDEX
%{rlibdir}/gRapHD/Meta
%{rlibdir}/gRapHD/R
%{rlibdir}/gRapHD/LICENSE
%{rlibdir}/gRapHD/help
%{rlibdir}/gRapHD/libs
%{rlibdir}/gRapHD/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2-1
- initial package for Fedora