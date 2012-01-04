%global packname  parody
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Parametric And Resistant Outlier DYtection

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-tools R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-tools R-utils 

%description
routines for univariate and multivariate outlier detection with a focus on
parametric methods, but support for some methods based on resistant

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
%doc %{rlibdir}/parody/NEWS
%doc %{rlibdir}/parody/html
%doc %{rlibdir}/parody/doc
%doc %{rlibdir}/parody/DESCRIPTION
%{rlibdir}/parody/help
%{rlibdir}/parody/Meta
%{rlibdir}/parody/data
%{rlibdir}/parody/R
%{rlibdir}/parody/NAMESPACE
%{rlibdir}/parody/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora