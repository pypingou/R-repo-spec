%global packname  picante
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          R tools for integrating phylogenies and ecology

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ape R-vegan R-nlme 


BuildRequires:    R-devel tex(latex) R-ape R-vegan R-nlme



%description
Phylocom integration, community analyses, null-models, traits and
evolution in R

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.0-1
- initial package for Fedora