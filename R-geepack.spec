%global packname  geepack
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Generalized Estimating Equation Package

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Generalized estimating equations solver for parameters in mean, scale, and
correlation structures, through mean link, scale link, and correlation
link. Can also handle clustered categorical responses.

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
%doc %{rlibdir}/geepack/doc
%doc %{rlibdir}/geepack/html
%doc %{rlibdir}/geepack/DESCRIPTION
%doc %{rlibdir}/geepack/CITATION
%{rlibdir}/geepack/help
%{rlibdir}/geepack/include
%{rlibdir}/geepack/INDEX
%{rlibdir}/geepack/Meta
%{rlibdir}/geepack/libs
%{rlibdir}/geepack/R
%{rlibdir}/geepack/data
%{rlibdir}/geepack/NAMESPACE

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora