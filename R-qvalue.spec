%global packname  qvalue
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Q-value estimation for false discovery rate control

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package takes a list of p-values resulting from the simultaneous
testing of many hypotheses and estimates their q-values. The q-value of a
test measures the proportion of false positives incurred (called the false
discovery rate) when that particular test is called significant. Various
plots are automatically generated, allowing one to make sensible
significance cut-offs. Several mathematical results have recently been
shown on the conservative accuracy of the estimated q-values from this
software. The software can be applied to problems in genomics, brain
imaging, astrophysics, and data mining.

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
%doc %{rlibdir}/qvalue/html
%doc %{rlibdir}/qvalue/DESCRIPTION
%doc %{rlibdir}/qvalue/doc
%{rlibdir}/qvalue/help
%{rlibdir}/qvalue/Meta
%{rlibdir}/qvalue/data
%{rlibdir}/qvalue/NAMESPACE
%{rlibdir}/qvalue/INDEX
%{rlibdir}/qvalue/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora