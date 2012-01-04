%global packname  mlegp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.1.2
Release:          1%{?dist}
Summary:          Maximum Likelihood Estimates of Gaussian Processes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Maximum likelihood Gaussian process modeling for univariate and
multi-dimensional outputs with diagnostic plots. Contact the maintainer
for a package version that implements sensitivity analysis functionality.

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
%doc %{rlibdir}/mlegp/html
%doc %{rlibdir}/mlegp/DESCRIPTION
%doc %{rlibdir}/mlegp/doc
%{rlibdir}/mlegp/libs
%{rlibdir}/mlegp/Meta
%{rlibdir}/mlegp/NAMESPACE
%{rlibdir}/mlegp/R
%{rlibdir}/mlegp/INDEX
RPM build errors:
%{rlibdir}/mlegp/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.1.2-1
- initial package for Fedora