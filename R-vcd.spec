%global packname  vcd
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.12
Release:          1%{?dist}
Summary:          Visualizing Categorical Data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-grid R-colorspace 

BuildRequires:    R-devel tex(latex) R-MASS R-grid R-colorspace 

%description
Visualization techniques, data sets, summary and inference procedures
aimed particularly at categorical data. Special emphasis is given to
highly extensible grid graphics. The package was inspired by the book
"Visualizing Categorical Data" by Michael Friendly.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.12-1
- initial package for Fedora