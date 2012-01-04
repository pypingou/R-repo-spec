%global packname  scaleboot
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.3
Release:          1%{?dist}
Summary:          Approximately Unbiased P-values via Multiscale Bootstrap

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Calculating approximately unbiased (AU) p-values from multiscale bootstrap

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
%doc %{rlibdir}/scaleboot/doc
%doc %{rlibdir}/scaleboot/html
%doc %{rlibdir}/scaleboot/DESCRIPTION
%{rlibdir}/scaleboot/help
%{rlibdir}/scaleboot/INDEX
%{rlibdir}/scaleboot/data
%{rlibdir}/scaleboot/Meta
%{rlibdir}/scaleboot/NAMESPACE
%{rlibdir}/scaleboot/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.3-1
- initial package for Fedora