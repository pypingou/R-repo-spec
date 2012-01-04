%global packname  NBDdirichlet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.01
Release:          1%{?dist}
Summary:          NBD-Dirichlet model of consumer buying behavior for marketing research

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The Dirichlet (aka NBD-Dirichlet) model describes the purchase incidence
and brand choice of consumer products.  We estimate the model and
summarize various theoretical quantities of interest to marketing
researchers. Also provides functions for making tables that compare
observed and theoretical statistics.

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
%doc %{rlibdir}/NBDdirichlet/DESCRIPTION
%doc %{rlibdir}/NBDdirichlet/doc
%doc %{rlibdir}/NBDdirichlet/html
%{rlibdir}/NBDdirichlet/help
%{rlibdir}/NBDdirichlet/Meta
%{rlibdir}/NBDdirichlet/R
%{rlibdir}/NBDdirichlet/INDEX
%{rlibdir}/NBDdirichlet/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.01-1
- initial package for Fedora