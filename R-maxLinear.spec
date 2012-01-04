%global packname  maxLinear
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Conditional Samplings for Max-Linear Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Computational tools for conditional samplings from max-linear models.

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
%doc %{rlibdir}/maxLinear/html
%doc %{rlibdir}/maxLinear/CITATION
%doc %{rlibdir}/maxLinear/DESCRIPTION
%{rlibdir}/maxLinear/NAMESPACE
%{rlibdir}/maxLinear/INDEX
%{rlibdir}/maxLinear/demo
%{rlibdir}/maxLinear/help
%{rlibdir}/maxLinear/Meta
%{rlibdir}/maxLinear/R
%{rlibdir}/maxLinear/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora