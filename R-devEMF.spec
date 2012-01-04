%global packname  devEMF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.4
Release:          1%{?dist}
Summary:          EMF graphics output device

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grDevices 

BuildRequires:    R-devel tex(latex) R-grDevices 

%description
Output graphics to EMF (enhanced metafile).

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
%doc %{rlibdir}/devEMF/html
%doc %{rlibdir}/devEMF/NEWS
%doc %{rlibdir}/devEMF/DESCRIPTION
%{rlibdir}/devEMF/INDEX
%{rlibdir}/devEMF/NAMESPACE
%{rlibdir}/devEMF/Meta
%{rlibdir}/devEMF/libs
%{rlibdir}/devEMF/R
%{rlibdir}/devEMF/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.4-1
- initial package for Fedora