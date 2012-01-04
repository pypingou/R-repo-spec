%global packname  mxkssd
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Efficient mixed-level k-circulant supersaturated designs

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
mxkssd is a package that generates efficient balanced mixed-level
k-circulant supersaturated designs by interchanging the elements of the
generator vector. The package tries to generate a supersaturated design
that has EfNOD efficiency more than user specified efficiency level (mef).
The package also displays the progress of generation of an efficient
mixed-level k-circulant design through a progress bar. The progress of 100
per cent means that one full round of interchange is completed. More than
one full round (typically 4-5 rounds) of interchange may be required for
larger designs.

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
%doc %{rlibdir}/mxkssd/DESCRIPTION
%doc %{rlibdir}/mxkssd/html
%{rlibdir}/mxkssd/R
%{rlibdir}/mxkssd/Meta
%{rlibdir}/mxkssd/help
%{rlibdir}/mxkssd/INDEX
%{rlibdir}/mxkssd/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora