%global packname  FGN
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Fractional Gaussian Noise, estimation and simulaton

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ltsa 

BuildRequires:    R-devel tex(latex) R-ltsa 

%description
MLE for H parameter in FGN; MLE for regression with FGN error; simulation
of FGN; print, summary, plot, coef, residuals, Boot methods.

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
%doc %{rlibdir}/FGN/NEWS
%doc %{rlibdir}/FGN/html
%doc %{rlibdir}/FGN/DESCRIPTION
%doc %{rlibdir}/FGN/doc
%doc %{rlibdir}/FGN/CITATION
%{rlibdir}/FGN/data
%{rlibdir}/FGN/Meta
%{rlibdir}/FGN/NAMESPACE
%{rlibdir}/FGN/INDEX
%{rlibdir}/FGN/R
%{rlibdir}/FGN/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora