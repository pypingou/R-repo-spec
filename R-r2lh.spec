%global packname  r2lh
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7
Release:          1%{?dist}
Summary:          R to LaTeX and HTML

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
generate univariate and bivariate analyses in LaTeX or HTML formats

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
%doc %{rlibdir}/r2lh/html
%doc %{rlibdir}/r2lh/DESCRIPTION
%doc %{rlibdir}/r2lh/doc
%{rlibdir}/r2lh/data
%{rlibdir}/r2lh/R
%{rlibdir}/r2lh/NAMESPACE
%{rlibdir}/r2lh/INDEX
%{rlibdir}/r2lh/help
%{rlibdir}/r2lh/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7-1
- initial package for Fedora