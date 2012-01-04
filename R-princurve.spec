%global packname  princurve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.11
Release:          1%{?dist}
Summary:          Fits a Principal Curve in Arbitrary Dimension

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
fits a principal curve to a data matrix in arbitrary dimensions

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
%doc %{rlibdir}/princurve/DESCRIPTION
%doc %{rlibdir}/princurve/html
%{rlibdir}/princurve/R
%{rlibdir}/princurve/INDEX
%{rlibdir}/princurve/NAMESPACE
%{rlibdir}/princurve/Meta
%{rlibdir}/princurve/libs
%{rlibdir}/princurve/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.11-1
- initial package for Fedora