%global packname  clst
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Classification by local similarity threshold

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-ROC R-lattice 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-ROC R-lattice 


%description
Package for modified nearest-neighbor classification based on calculation
of a similarity threshold distinguishing within-group from between-group

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
%doc %{rlibdir}/clst/doc
%doc %{rlibdir}/clst/DESCRIPTION
%doc %{rlibdir}/clst/html
%{rlibdir}/clst/NAMESPACE
%{rlibdir}/clst/INDEX
%{rlibdir}/clst/R
%{rlibdir}/clst/help
%{rlibdir}/clst/Meta
%{rlibdir}/clst/data

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora