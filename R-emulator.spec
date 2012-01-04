%global packname  emulator
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.8
Release:          1%{?dist}
Summary:          Bayesian emulation of computer programs

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
This package allows one to estimate the output of a computer program, as a
function of the input parameters, without actually running it. The
computer program is assumed to be a Gaussian process, whose parameters are
estimated using Bayesian techniqes that give a PDF of expected program
output. This PDF is conditional on a ``training set'' of runs, each
consisting of a point in parameter space and the model output at that
point.  The emphasis is on complex codes that take weeks or months to run,
and that have a large number of undetermined input parameters; many
climate prediction models fall into this class.  The emulator essentially
determines Bayesian a-postiori estimates of the PDF of the output of a
model, conditioned on results from previous runs and a user-specified
prior linear model.  A working example is given in the help page for
function `interpolant()', which should be the first point of reference.

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
%doc %{rlibdir}/emulator/CITATION
%doc %{rlibdir}/emulator/html
%doc %{rlibdir}/emulator/DESCRIPTION
%doc %{rlibdir}/emulator/doc
%{rlibdir}/emulator/help
%{rlibdir}/emulator/INDEX
%{rlibdir}/emulator/Meta
%{rlibdir}/emulator/data
%{rlibdir}/emulator/R
%{rlibdir}/emulator/NAMESPACE
RPM build errors:

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.8-1
- initial package for Fedora