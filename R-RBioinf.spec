%global packname  RBioinf
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          RBioinf

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph R-methods 

BuildRequires:    R-devel tex(latex) R-graph R-methods 

%description
Functions and datasets and examples to accompany the monograph R For

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
%doc %{rlibdir}/RBioinf/DESCRIPTION
%doc %{rlibdir}/RBioinf/doc
%doc %{rlibdir}/RBioinf/html
%{rlibdir}/RBioinf/INDEX
%{rlibdir}/RBioinf/NAMESPACE
%{rlibdir}/RBioinf/help
%{rlibdir}/RBioinf/schema
%{rlibdir}/RBioinf/Exercises
%{rlibdir}/RBioinf/Meta
%{rlibdir}/RBioinf/R
%{rlibdir}/RBioinf/libs
%{rlibdir}/RBioinf/extdata

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora