%global packname  RnavGraphImageData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Some image data used in the RnavGraph package demos

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Image data used as examples in the RnavGraph R package. See the demos in
the RnavGraph package.

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
%doc %{rlibdir}/RnavGraphImageData/html
%doc %{rlibdir}/RnavGraphImageData/DESCRIPTION
%{rlibdir}/RnavGraphImageData/R
%{rlibdir}/RnavGraphImageData/INDEX
%{rlibdir}/RnavGraphImageData/help
%{rlibdir}/RnavGraphImageData/NAMESPACE
%{rlibdir}/RnavGraphImageData/aloi_small
%{rlibdir}/RnavGraphImageData/Meta
%{rlibdir}/RnavGraphImageData/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora