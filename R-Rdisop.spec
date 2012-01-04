%global packname  Rdisop
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          Decomposition of Isotopic Patterns

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Identification of metabolites using high precision mass spectrometry. MS
Peaks are used to derive a ranked list of sum formulae, alternatively for
a given sum formula the theoretical isotope distribution can be calculated
to search in MS peak lists.

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
%doc %{rlibdir}/Rdisop/html
%doc %{rlibdir}/Rdisop/DESCRIPTION
%doc %{rlibdir}/Rdisop/doc
%{rlibdir}/Rdisop/libs
%{rlibdir}/Rdisop/unitTests
%{rlibdir}/Rdisop/Rcpp-license.txt
%{rlibdir}/Rdisop/Meta
%{rlibdir}/Rdisop/help
%{rlibdir}/Rdisop/R
%{rlibdir}/Rdisop/INDEX
%{rlibdir}/Rdisop/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora