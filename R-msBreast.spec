%global packname  msBreast
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Protein Mass Spectra Dataset from a Breast Cancer Study

Group:            Applications/Engineering 
License:          GNU General Public License Version 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides a dataset of 96 protein mass spectra generated from
a pooled sample of nipple aspirate fluid (NAF) from healthy breasts and
breasts with cancer.

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
%doc %{rlibdir}/msBreast/html
%doc %{rlibdir}/msBreast/doc
%doc %{rlibdir}/msBreast/DESCRIPTION
%{rlibdir}/msBreast/data
%{rlibdir}/msBreast/Meta
%{rlibdir}/msBreast/NAMESPACE
%{rlibdir}/msBreast/INDEX
%{rlibdir}/msBreast/LICENSE
%{rlibdir}/msBreast/help
RPM build errors:

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora