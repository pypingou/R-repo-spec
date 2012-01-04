%global packname  visualizationTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.04
Release:          1%{?dist}
Summary:          Package contains a few functions to visualize statistical circumstances.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils R-stats R-grDevices R-graphics 

BuildRequires:    R-devel tex(latex) R-utils R-stats R-grDevices R-graphics 

%description
Package contains function to visualize a t-test, the power of a t-test,
control charts and the influence of regulating them, Oc-curves, the Law of
large Numbers and confidence intervals.

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
%doc %{rlibdir}/visualizationTools/doc
%doc %{rlibdir}/visualizationTools/DESCRIPTION
%doc %{rlibdir}/visualizationTools/html
%{rlibdir}/visualizationTools/NAMESPACE
%{rlibdir}/visualizationTools/help
%{rlibdir}/visualizationTools/R
%{rlibdir}/visualizationTools/INDEX
%{rlibdir}/visualizationTools/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.04-1
- initial package for Fedora