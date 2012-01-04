%global packname  lfe
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.709
Release:          1%{?dist}
Summary:          Linear Group Fixed Effects

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-709.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Matrix 

%description
Estimate linear models with multiple group fixed effects

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
%doc %{rlibdir}/lfe/html
%doc %{rlibdir}/lfe/doc
%doc %{rlibdir}/lfe/DESCRIPTION
%doc %{rlibdir}/lfe/CITATION
%{rlibdir}/lfe/INDEX
%{rlibdir}/lfe/help
%{rlibdir}/lfe/TODO
%{rlibdir}/lfe/exec
%{rlibdir}/lfe/Meta
%{rlibdir}/lfe/R
%{rlibdir}/lfe/libs
%{rlibdir}/lfe/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.709-1
- initial package for Fedora