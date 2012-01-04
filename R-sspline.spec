%global packname  sspline
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Smoothing Splines on the Sphere

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
R package for Computing the Spherical Smoothing Splines

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
%doc %{rlibdir}/sspline/DESCRIPTION
%doc %{rlibdir}/sspline/html
%{rlibdir}/sspline/libs
%{rlibdir}/sspline/help
%{rlibdir}/sspline/Meta
%{rlibdir}/sspline/data
%{rlibdir}/sspline/INDEX
%{rlibdir}/sspline/R
%{rlibdir}/sspline/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora