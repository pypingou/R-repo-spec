%global packname  cem
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.142
Release:          1%{?dist}
Summary:          CEM: Software for Coarsened Exact Matching

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-nlme R-lattice R-randomForest R-tcltk 

BuildRequires:    R-devel tex(latex) R-nlme R-lattice R-randomForest R-tcltk 

%description
This program implements the coarsened exact matching algorithm (and many
extensions) described in Stefano M. Iacus, Gary King, and Giuseppe Porro,
"Causal Inference Without Balance Checking: Coarsened Exact Matching,"

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.142-1
- initial package for Fedora