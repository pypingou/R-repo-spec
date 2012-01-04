%global packname  RColorBrewer
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          ColorBrewer palettes

Group:            Applications/Engineering 
License:          Apache License 2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The packages provides palettes for drawing nice maps shaded according to a

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
%doc %{rlibdir}/RColorBrewer/DESCRIPTION
%doc %{rlibdir}/RColorBrewer/html
%doc %{rlibdir}/RColorBrewer/COPYING
%{rlibdir}/RColorBrewer/help
%{rlibdir}/RColorBrewer/Meta
%{rlibdir}/RColorBrewer/R
%{rlibdir}/RColorBrewer/INDEX
%{rlibdir}/RColorBrewer/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora