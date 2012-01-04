%global packname  plugdensity
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.2
Release:          1%{?dist}
Summary:          Plug-in Kernel Density Estimation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Kernel density estimation with global bandwidth selection via "plug-in".

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
%doc %{rlibdir}/plugdensity/DESCRIPTION
%doc %{rlibdir}/plugdensity/html
%{rlibdir}/plugdensity/libs
%{rlibdir}/plugdensity/Meta
%{rlibdir}/plugdensity/INDEX
%{rlibdir}/plugdensity/help
%{rlibdir}/plugdensity/R
%{rlibdir}/plugdensity/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.2-1
- initial package for Fedora